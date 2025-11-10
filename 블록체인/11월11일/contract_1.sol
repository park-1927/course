/**
 * @title SimpleStorage
 * @dev 이 계약은 하나의 정수 값을 저장하고 검색하는 예제입니다.
 */
contract SimpleStorage {
    
    uint private data;

    /**
     * @notice 저장된 값을 업데이트합니다.
     * @dev 이 함수는 블록체인 상태를 변경하므로 가스가 소모됩니다.
     * @param _newValue 저장할 새로운 정수 값입니다.
     */
    function set(uint _newValue) public {
        data = _newValue;
    }

    /// @notice 현재 저장된 값을 반환합니다.
    /// @return The stored value.
    function get() public view returns (uint) {
        return data;
    }
}