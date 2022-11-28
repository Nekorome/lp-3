//SPDX-License-Identifier:MIT
pragma solidity 0.4.22;
contract Bank{
    int bal;
    constructor() public{
        bal = 100;
    }
    function getbalance()view public returns (int){
        return bal;
    }
    function withDraw(int amt) public{
        bal = bal - amt;
    }
    function deposit(int amt) public{
        bal = bal + amt;
    }
}
