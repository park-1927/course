const http = require('http');

// 서버가 접속을 대기할 포트 번호와 호스트 이름을 정의함
const hostname = '127.0.0.1'; // localhost
const port = 3000;

// 2. 서버를 생성함
	const server = http.createServer((req, res) => {
 	 // 요청(req)에 응답(res)하는 로직임
  
  		// 응답 헤더 설정: 성공(200) 상태 코드와 응답 타입(일반 텍스트)
  		res.statusCode = 200;
		res.setHeader('Content-Type', 'text/plain; charset=utf-8');

		// 사용자에게 보낼 실제 응답 본문
  		res.end('Node.js로 만든 아주 간단한 서버입니다!\n');
               });
// 3. 서버를 지정된 포트와 호스트 이름에서 대기(Listen)하도록 함
server.listen(port, hostname, () => {
console.log(`서버가 http://${hostname}:${port}/ 주소에서 실행 중입니다.`);
console.log('브라우저에서 이 주소로 접속해 보세요.');
});