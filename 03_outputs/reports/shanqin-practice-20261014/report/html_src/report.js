/* Enhancement only: report content is always derived from the current deck model. */
(function(root){
  'use strict';
  const original = root.CorporateReport;
  const expanded = new Set();
  let returnIndex = 1;
  let printState = [];
  const make=(tag,cls,text)=>{const n=document.createElement(tag);n.className=cls;if(text)n.textContent=text;return n;};
  root.CorporateReport=Object.freeze({clear:original.clear,render(host,deck,actions){
    const sections=original.render(host,deck,actions);
    const nav=host.querySelector('.report-nav');
    const allButtons=[...nav.querySelectorAll('[data-report-nav]')];
    nav.replaceChildren(make('p','report-eyebrow','阅读目录'));
    const groups=new Set();
    deck.slides.forEach((slide,index)=>{
      if(slide.layout==='cover'||groups.has(slide.section))return;
      groups.add(slide.section);
      const btn=allButtons[index];
      btn.replaceChildren(document.createTextNode(slide.section));
      nav.append(btn);
    });
    nav.append(make('p','report-nav-note','正文保留完整分析。点击 E 编号查阅证据；打印时自动展开全部证据。'));
    let addedIntro=false;
    deck.slides.forEach((slide,index)=>{
      const section=sections[index];
      section.dataset.contentId=slide.id;
      if(slide.id.startsWith('source-photo-')||slide.id.startsWith('operation-photo-'))section.classList.add('report-source-photo');
      const eyebrow=section.querySelector('.report-eyebrow');
      if(slide.layout!=='cover')eyebrow.textContent=slide.title===slide.section?'HK TECHNOLOGY · 内部管理讨论':slide.section;
      if(slide.layout==='cover'&&slide.title.includes('：')){
        const heading=section.querySelector('.report-heading');
        const split=slide.title.indexOf('：');
        heading.replaceChildren(document.createTextNode(slide.title.slice(0,split)+'：'),make('span','report-cover-subtitle',slide.title.slice(split+1)));
      }
      if(slide.title.endsWith('（续）')){
        section.classList.add('report-continuation');
        sections[index-1]?.classList.add('report-before-continuation');
      }
      if(!/^e\d{2}$/.test(slide.id))return;
      if(!addedIntro){
        const title=make('h2','report-heading','证据详情 E01–E24');
        const intro=make('p','evidence-intro','A：材料直接支持的事实；B：少量体验观察；C：分析推论；D：未验证假设或建议。高／中／低表示本项陈述的证据充分度，不是统计置信度或产品评级。来源代号见附录D。');
        const controls=make('div','evidence-controls');
        for(const [label,open] of [['展开全部',true],['收起全部',false]]){
          const b=make('button','',label);b.type='button';b.addEventListener('click',()=>host.querySelectorAll('.evidence-detail').forEach(d=>{d.open=open;open?expanded.add(d.dataset.evidence):expanded.delete(d.dataset.evidence);}));controls.append(b);
        }
        section.before(title,intro,controls);addedIntro=true;
      }
      const detail=make('details','evidence-detail');detail.dataset.evidence=slide.id;
      const summary=make('summary','',slide.title);detail.append(summary);
      detail.open=actions.editing||expanded.has(slide.id)||index===actions.current;
      detail.addEventListener('toggle',()=>{detail.open?expanded.add(slide.id):expanded.delete(slide.id);});
      section.before(detail);detail.append(section);
      const back=make('button','evidence-back','返回引用处');back.type='button';
      back.addEventListener('click',()=>actions.navigate(returnIndex));section.append(back);
    });
    if(host.citationCapture)host.removeEventListener('click',host.citationCapture,true);
    host.citationCapture=event=>{
      const link=event.target.closest('[data-hyperlink]');
      if(link&&/^#e\d{2}$/.test(link.dataset.hyperlink)){
        const owner=link.closest('[data-report-slide]');
        if(owner&&!/^e\d{2}$/.test(deck.slides[+owner.dataset.reportSlide]?.id))returnIndex=+owner.dataset.reportSlide;
      }
    };
    host.addEventListener('click',host.citationCapture,true);
    const footer=host.querySelector('.report-footer');
    footer.replaceChildren(make('span','','HK Technology · 内部管理讨论 · 2026年10月14日'),make('span','','正文依据最新更正报告；真实界面于2026年10月15日补采。离线文件，可打印。'));
    document.documentElement.lang='zh-CN';
    return sections;
  }});
  root.addEventListener('beforeprint',()=>{
    printState=[...document.querySelectorAll('.evidence-detail')].map(d=>[d,d.open]);
    for(const [detail] of printState)detail.open=true;
  });
  root.addEventListener('afterprint',()=>{
    for(const [detail,open] of printState)detail.open=open;
    printState=[];
  });
})(globalThis);
