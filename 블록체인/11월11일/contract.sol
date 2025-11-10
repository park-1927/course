// SPDX-License-Identifier: MIT

//pragma solidity ^0.8.0;

//pragma solidity ^0.7.2;

/**
 * @title Adder
 * @dev 두 개의 숫자를 받아 더한 결과를 반환하는 간단한 계약입니다.
 */
contract Adder {

    /**
     * @notice 두 정수를 더한 결과를 반환합니다.
     * @param _a 첫 번째 정수
     * @param _b 두 번째 정수
     * @return sum 두 정수의 합계
     */
    function add(uint _a, uint _b) public pure returns (uint sum) {
        // uint256 타입의 오버플로우/언더플로우는 Solidity 0.8.0 버전부터 자동으로 체크됩니다.
        return _a + _b;
    }
}