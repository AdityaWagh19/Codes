// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract Bank {

    mapping(address => uint) public user_account;
    mapping(address => bool) public user_exist;

    function create_account() public payable returns(string memory) {

        require(
            user_exist[msg.sender] == false,
            "Account Already created!"
        );

        user_account[msg.sender] = msg.value;
        user_exist[msg.sender] = true;

        return "Account created";
    }

    function deposit(uint amount)
        public
        payable
        returns(string memory)
    {
        require(
            user_exist[msg.sender] == true,
            "Account not created!"
        );

        require(amount > 0);

        user_account[msg.sender] += amount;

        return "Amount deposited successfully";
    }

    function withdraw(uint amount)
        public
        returns(string memory)
    {
        require(
            user_exist[msg.sender] == true,
            "Account not created!"
        );

        require(amount > 0);

        require(
            user_account[msg.sender] >= amount,
            "Insufficient balance"
        );

        user_account[msg.sender] -= amount;

        return "Amount withdrawn successfully";
    }

    function account_balance()
        public
        view
        returns(uint)
    {
        return user_account[msg.sender];
    }

    function account_exists()
        public
        view
        returns(bool)
    {
        return user_exist[msg.sender];
    }
}
