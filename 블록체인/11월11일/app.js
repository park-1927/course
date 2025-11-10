import { greet, fetchData } from './utils.js';

// Top-level await 사용 (최신 Node.js 기능)
console.log('--- 1. 일반 함수 실행 ---');
const message = greet('개발자');
console.log(message);

console.log('\n--- 2. 비동기 함수 실행 (Top-level await) ---');
try {
    const todoTitle = await fetchData();
    console.log(`비동기 데이터: ${todoTitle}`);
} catch (error) {
    console.error('데이터를 가져오는 중 오류 발생:', error);
}

// Node.js 내장 모듈 가져오기 (import 'node:' 접두사 권장)
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname } from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

console.log('\n--- 3. Node.js 내장 모듈 사용 (ESM) ---');
console.log(`현재 파일 경로: ${__filename}`);
// ... 파일 읽기 등의 비동기 작업을 await로 바로 처리 가능