Account = {balance = 0}

function Account:new (o)
o = o or {}
setmetatable(o, self)
self.__index = self
return o
end

function Account:deposit (v)
self.balance = self.balance + v
end

function Account:withdraw (v)
if v > self.balance then
error"insufficient funds"
end
self.balance = self.balance - v
end

player = Account:new()
print("new account balance: "..player.balance)

player:deposit(2500)
print("new account balance after deposit: "..player.balance)

player:withdraw(50)
print("new account balance after withdrawal: "..player.balance)