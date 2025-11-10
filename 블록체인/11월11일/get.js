// getLatestBlock.js 파일 내용

// 1. web3 라이브러리를 불러옵니다.
const { Web3 } = require('web3');

// 2. 사용할 RPC 엔드포인트 URL을 정의합니다.
const rpcURL = 'https://eth.llamarpc.com';

// 3. Web3 인스턴스를 생성하고, RPC 엔드포인트를 프로바이더로 설정합니다.
const web3 = new Web3(rpcURL);

/**
 * 최신 블록 번호를 가져오는 함수
 */
async function getLatestBlockNumber() {
    console.log(`📡 RPC 엔드포인트: ${rpcURL} 에 접속합니다...`);
    
    try {
        // eth.getBlockNumber() 메서드를 사용하여 최신 블록 번호를 요청합니다.
        const blockNumber = await web3.eth.getBlockNumber();
        
        console.log('--------------------------------------------------');
        console.log(`✅ 현재 이더리움의 최신 블록 번호는: ${blockNumber}`);
        console.log('--------------------------------------------------');
        
    } catch (error) {
        console.error('❌ 블록체인 정보 조회 중 오류가 발생했습니다:', error.message);
    }
}

// 함수를 실행합니다.
getLatestBlockNumber();