import { sveltekit } from '@sveltejs/kit/vite';
import type { UserConfig } from 'vite';

const config: UserConfig = {
	plugins: [sveltekit()],
	server: {
		watch: {
			usePolling: !!process.env.IS_WSL // Will lead to very high CPU usage, only for WSL users who would not prefer running code editors on WSL
		}
	}
};

export default config;
