# Assignment 4: Student Data Smart Contract (StudentManagement.sol)

Tools: Remix IDE, MetaMask wallet, Sepolia testnet (needs some Sepolia ETH from a faucet).

## Steps
1. **Compile:** In Remix, create `StudentManagement.sol` under `contracts/`, paste the code, open the *Solidity Compiler* tab and click **Compile StudentManagement.sol**.
2. **Deploy to Sepolia:** In *Deploy & Run Transactions*, set **Environment** to *Browser Extension / Injected Provider - MetaMask* (Sepolia network). Keep **Value = 0**, select `StudentManagement`, click **Deploy**, then **Confirm** in MetaMask.
3. **See the functions:** Under *Deployed Contracts*, expand the contract. It lists `addStudent`, `getStudent`, `studentCount`, plus the public getters `owner`, `students` and `totalReceived`.
4. **Add 2 students:** Call `addStudent` with `1, "John", 90`, confirm in MetaMask. Call it again with `2, "Sam", 100`, confirm again.
5. **Count students:** Click **studentCount** (Call). It returns `2`.
6. **Read a student:** Enter index `1` in **getStudent** and click Call. It returns `2, Sam, 100` (index `0` gives John).
7. **Test fallback:** Open **Low level interactions**, enter calldata `0x1234`, set Value to `1 wei` and click **Transact**, then confirm. Calldata that matches no function triggers `fallback()`. Sending ETH with empty calldata triggers `receive()`. Both add to `totalReceived`.
8. **Etherscan:** Open the contract address on `sepolia.etherscan.io`. The Transactions tab shows 2 `Add Student` transactions and 2 1-wei `Transfer` transactions. The contract's ETH balance is 2 wei.

## Notes
- `getStudent`, `studentCount` and the public getters are `view` calls and need no MetaMask confirmation.
- `addStudent` has no access control, so anyone can add students. `owner` is stored but not used.
