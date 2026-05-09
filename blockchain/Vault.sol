// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Vault {
    struct Entry {
        string label;
        string encryptedPassword;
    }

    mapping(address => Entry[]) private userVault;

    function storePassword(string memory label, string memory encryptedPassword) public {
        userVault[msg.sender].push(Entry(label, encryptedPassword));
    }

    function getPasswords() public view returns (Entry[] memory) {
        return userVault[msg.sender];
    }
}
