<template>
	<div class="container" v-loading="loading">
		<div>
			<el-input v-model="content" placeholder="填写需要纠错的文字" :autosize="{ minRows: 4}" type="textarea" class="handle-input mr10"></el-input>
		</div>

		<div style="margin-top: 10px;">
			<el-button type="primary" @click="run">纠错</el-button>
		</div>
		<div style="margin-top: 10px;">
			<el-input v-model="result" placeholder="纠错后的文字" disabled='true' :autosize="{ minRows: 4}" type="textarea" class="handle-input mr10"></el-input>
		</div>


	</div>



</template>
<script setup lang="ts" name="correction">
import { ref, reactive, onMounted} from 'vue';
import { correction} from '../api/index';

const loading = ref(false)
const query = reactive({content: ''});
const result = ref('')
const content = ref('')

const run = async () => {
	loading.value = true
	await correction(content.value).then(res =>{
		if (res.status == 200) {
				console.log(res.data)
				result.value = "[修正后的文本]:\n" + res.data['choices'][0]["text"];
				loading.value = false
			} else {
				loading.value = false
			}
	}).catch(err =>{
		result.value = err
		loading.value = false
	})
}

</script>
<style>
.container{
	height: 100%;
}

</style>