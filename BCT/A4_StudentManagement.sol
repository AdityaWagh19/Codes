// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract StudentManagement {

    struct Student {
        uint id;
        string name;
        uint marks;
    }

    Student[] public students;

    address public owner;
    uint public totalReceived;

    constructor() {
        owner = msg.sender;
    }

    function addStudent(
        uint _id,
        string memory _name,
        uint _marks
    ) public {

        students.push(
            Student(_id, _name, _marks)
        );
    }

    function getStudent(uint index)
        public
        view
        returns(
            uint,
            string memory,
            uint
        )
    {
        Student memory s = students[index];

        return (
            s.id,
            s.name,
            s.marks
        );
    }

    function studentCount()
        public
        view
        returns(uint)
    {
        return students.length;
    }

    receive() external payable {
        totalReceived += msg.value;
    }

    fallback() external payable {
        totalReceived += msg.value;
    }
}
