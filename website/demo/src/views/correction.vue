<template>
	<div class="container" v-loading="loading">
		<div>
			<el-input v-model="content" placeholder="填写需要纠错的文字" :autosize="{ minRows: 4}" type="textarea" class="handle-input mr10"></el-input>
		</div>

		<div style="margin-top: 10px;">
			<el-button type="primary" @click="run">纠错</el-button>
		</div>
		<div class="error">{{ error }}</div>
		<div style="margin-top: 10px;">
			<div id="view" class="code-contrast"></div>
		</div>
	</div>



</template>
<script setup lang="ts" name="correction">
import { ref, reactive, onMounted} from 'vue';
import { correction} from '../api/index';
import CodeMirror from "codemirror";
import "codemirror/lib/codemirror.css";
import "codemirror/addon/merge/merge.js"
import "codemirror/addon/merge/merge.css"
import DiffMatchPatch from "diff-match-patch";
window.diff_match_patch = DiffMatchPatch;
window.DIFF_DELETE = -1;
window.DIFF_INSERT = 1;
window.DIFF_EQUAL = 0;

const loading = ref(false)
const content = ref('')
const error = ref('')

const run = async () => {
	loading.value = true
	var target = document.getElementById("view");
	target.innerHTML = "";
	await correction(content.value).then(res =>{
		if (res.status == 200) {
				if(res.data.data && res.data.data.success){
					var correct_content = res.data.data.response
					correct_content = correct_content.replace("修改后：", "").replace("修改后:", "")
					CodeMirror.MergeView(target, {
						value: content.value,//上次内容
						origLeft: null,
						orig: correct_content,//本次内容
						lineNumbers: true,//显示行号
						mode: "text/html",
						hightlightDifference: "true",
						connect: null,
						revertButtons:false,
						readOnly: true,
						theme: "dracula",
						lineWrapping: true
						});
					loading.value = false
					error.value = ''
				}
				else{
					error.value = "HTTP Error: " + res.data.data.response
					loading.value = false
				}
				
			} else {
				error.value = "HTTP Error: " + res.status
				loading.value = false
			}
	}).catch(err =>{
		error.value = err
		loading.value = false
	})
}

</script>
<style>
.container{
	height: 100%;
	min-height: 400px;
}
.code-contrast {
  margin-top: 20px;
  text-align: left;
}

.CodeMirror{
	height: auto;
}

.CodeMirror-merge-2pane .CodeMirror-merge-gap{
	width: 0%;
	display: none;
}

.CodeMirror-merge-2pane .CodeMirror-merge-editor{
	display: none;
	width: 0%;
}

.CodeMirror-merge-2pane .CodeMirror-merge-pane{
	width: 100%;
}

.CodeMirror-merge-r-deleted{
	color: red;
}

.CodeMirror-merge-r-inserted{
	color: blue;
}

.error{
	margin-top: 20px;
	color: red;
}

</style>