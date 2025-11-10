// web3 라이브러리 불러오기

const { Web3 } = require('web3');

// 💡 중요: 블록체인 노드에 접근하기 위한 RPC 엔드포인트 URL
// 실제 서비스에서는 Infura, Alchemy 등의 계정을 만들어 사용
// 이 예제에서는 공개적으로 접근 가능한 이더리움 메인넷 RPC를 사용

const rpcURL = 'https://eth.llamarpc.com'; 

// Web3 인스턴스 생성 및 노드에 연결
const web3 = new Web3(rpcURL);

async function getLatestBlockNumber() {
    try {
        console.log("이더리움 블록체인에 연결 중...");

        // web3.eth.getBlockNumber() 메서드를 사용하여 최신 블록 번호를 요청
        const blockNumber = await web3.eth.getBlockNumber();

        console.log('-------------------------------------------');
        console.log(`✅ 현재 이더리움 블록 번호: ${blockNumber.toString()}`);
        console.log('-------------------------------------------');
        console.log('이것이 Web3를 사용하여 블록체인 데이터를 읽는 기본 동작입니다.');
        
    } catch (error) {
        console.error('❌ 블록체인 연결 또는 조회 중 오류 발생:', error);
    }
}

// 함수 실행
getLatestBlockNumber();