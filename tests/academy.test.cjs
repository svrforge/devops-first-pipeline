const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const core=require('../academy/core.js');
test('hash routing rejects missing, malformed and out-of-range days',()=>{for(const value of ['','#day=0','#day=31','#day=x','#foo=3'])assert.equal(core.dayFromHash(value),1);assert.equal(core.dayFromHash('#day=30'),30);assert.equal(core.dayFromHash('#day=07'),7);});
test('stored progress is bounded and deduplicated',()=>{assert.deepEqual(core.cleanState({done:['01','01','99'],quiz:{'01':true,'99':true},lab:{'01':false},notes:{'02':'hello'}}),{done:['01'],quiz:{'01':true},lab:{},notes:{'02':'hello'}});assert.deepEqual(core.cleanState(null).done,[]);assert.equal(core.cleanState({notes:{'01':'x'.repeat(11000)}}).notes['01'].length,10000);});
test('completion requires both quiz understanding and lab evidence',()=>{const state=core.cleanState(null);assert.equal(core.canComplete(state,'01'),false);state.quiz['01']=true;assert.equal(core.canComplete(state,'01'),false);state.lab['01']=true;assert.equal(core.canComplete(state,'01'),true);assert.equal(core.canComplete(state,'99'),false);});
test('bundled course matches canonical content',()=>{const context={window:{}};vm.runInNewContext(fs.readFileSync('academy/course-data.js','utf8'),context);const data=JSON.parse(JSON.stringify(context.window.COURSE));assert.deepEqual(data,JSON.parse(fs.readFileSync('course/catalog.json','utf8')));assert.equal(data.lessons.length,30);assert.equal(core.filterLessons(data.lessons,'TERRAFORM')[0].day,23);assert.equal(core.filterLessons(data.lessons,'nothing-matches').length,0);for(const l of data.lessons){assert.equal(l.steps.length,4);assert.equal(l.visual.length,4);}});
