local tools = require("addons/tools")

local marketAccount = {balance = 0}
    
    function marketAccount:new (o)
      o = o or {}
      setmetatable(o, self)
      self.__index = self
      return o
    end
    
    function marketAccount:deposit (v)
      self.balance = self.balance + v
    end
    
    function marketAccount:withdraw (v)
      if v > self.balance then tools.error(player, "Insufficient funds.\nYour balance: "..self.balance, true) end
      self.balance = self.balance - v
    end
    