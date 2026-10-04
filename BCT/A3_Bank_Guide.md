# Assignment 3: Bank Smart Contract (Bank.sol)

Tools: Remix IDE, MetaMask wallet, Sepolia testnet (needs some Sepolia ETH from a faucet).

## Steps
1. **Compile:** In Remix, create `Bank.sol` under `contracts/`, paste the code, open the *Solidity Compiler* tab and click **Compile Bank.sol** (compiler `^0.8.18`).
2. **Deploy to Sepolia:** Open *Deploy & Run Transactions*. Set **Environment** to *Browser Extension / Injected Provider - MetaMask*. Unlock MetaMask, select the Sepolia network and your account. Keep **Value = 0**, select `Bank`, click **Deploy**, then **Confirm** in the MetaMask popup. (Optional: keep "Verify Contract on Explorers" on.)
3. **See the functions:** Under *Deployed Contracts*, expand the contract. It lists `create_account`, `deposit`, `withdraw`, `account_balance`, `account_exists`, plus the public getters `user_account` and `user_exist`.
4. **Create account:** Set **Value = 1 wei**, click **create_account** (Transact), confirm in MetaMask.
5. **Check account exists:** Click **account_exists** (Call). It returns `true`.
6. **Deposit:** Enter `500` as `amount`, Value `1 wei`, click **deposit**, confirm in MetaMask.
7. **Withdraw:** Enter `1` as `amount`, Value `0`, click **withdraw**, confirm in MetaMask.
8. **Check balance:** Click **account_balance** (Call). It returns `500` (1 + 500 - 1).
9. **Etherscan:** Copy the contract address and open it on `sepolia.etherscan.io`. The Transactions tab lists `Create_account`, `Deposit` and `Withdraw`. The contract's ETH balance is 2 wei (the two 1-wei payments).

## Notes
- `view` functions (`account_exists`, `account_balance`) are free calls and need no MetaMask confirmation.
- `deposit` adds the `amount` argument to the balance, not `msg.value`, and `withdraw` only reduces the stored balance (it does not send ETH). That is why the balance shows 500 while the contract holds only 2 wei. Fine for a demo, not for real funds.
