/* Pure helpers shared by the browser and Node tests. */
(function(root){
'use strict';
const ids=Array.from({length:30},(_,i)=>String(i+1).padStart(2,'0'));
function dayFromHash(hash){const match=/^#day=(\d{1,2})$/.exec(hash);const day=match?Number(match[1]):1;return day>=1&&day<=30?day:1;}
function cleanState(raw){const empty={done:[],quiz:{},lab:{},notes:{}};if(!raw||typeof raw!=='object'||Array.isArray(raw))return empty;
empty.done=Array.isArray(raw.done)?[...new Set(raw.done.filter(id=>ids.includes(id)))]:[];
for(const key of ['quiz','lab','notes']){if(!raw[key]||typeof raw[key]!=='object')continue;for(const id of ids){const v=raw[key][id];if(key==='notes'&&typeof v==='string')empty.notes[id]=v.slice(0,10000);else if(key!=='notes'&&v===true)empty[key][id]=true;}}
return empty;}
function canComplete(state,id){return ids.includes(id)&&state.quiz[id]===true&&state.lab[id]===true;}
function filterLessons(lessons,query){const q=query.trim().toLowerCase();return lessons.filter(l=>`${l.day} ${l.title.en} ${l.phase}`.toLowerCase().includes(q));}
const api={dayFromHash,cleanState,canComplete,filterLessons};if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.AcademyCore=api;
})(typeof window!=='undefined'?window:this);
