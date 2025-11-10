export const greet = (name) => {
    return `안녕하세요, ${name}님! (ESM)`;
};

// 2. 비동기 함수 (Top-level await 가능)
export async function fetchData() {
    // 최신 Node.js는 fetch API를 내장하고 있음
    const response = await 
fetch('https://jsonplaceholder.typicode.com/todos/1'); 
    const data = await response.json();
    return data.title;
}