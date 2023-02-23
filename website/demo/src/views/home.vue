<template>
	<v-header />
	<div class="content-box">
		<div class="content">
			<router-view v-slot="{ Component }">
				<component :is="Component"></component>
			</router-view>
		</div>
	</div>
</template>
<script setup lang="ts">
import vHeader from '../components/header.vue';
</script>
