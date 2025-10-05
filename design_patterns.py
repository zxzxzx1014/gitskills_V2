# 抽象狀態類
class LiftState:

  def Open(self):
    pass
  def Close(self):
    pass
  def Run(self):
    pass
  def Stop(self):
    pass
  def LlightUp(self):
    pass

# 具體狀態：運行
class RunState(LiftState):
  def Open(self):
    print("RUN:Open Forbidden.")
    return self
  def Close(self):
    print("RUN:Close Forbidden.")
    return self
  def Run(self):
    print("RUN:The lift is running...")
    return self
  def Stop(self):
    print("RUN:The lift start to stop...")
    print("RUN:The lift stopped...")
    return StopState()

# 具體狀態：停止
class StopState(LiftState):

  def Open(self):
    print("STOP:The door is opening...")
    print("STOP:The door is opened...")
    return OpenState()

  def Close(self):
    print("STOP:Close Forbidden")
    return self
  def Run(self):
    print("STOP:The lift start to run...")
    return RunState()
  def Stop(self):
    print("STOP:The lift is stopped.")
    return self

# 具體狀態：開門
class OpenState(LiftState):

  def Open(self):
    print("OPEN:The door is opened...")
    return self

  def Close(self):
    print("OPEN:The door start to close...")
    print("OPEN:The door is closed")
    return StopState()

  def Run(self):
    print("OPEN:Run Forbidden.")
    return self

  def Stop(self):
    print("OPEN:Stop Forbidden.")
    return self

# 環境類：負責保存當前狀態並調用對應操作
class Context:
  lift_state = ""

  def GetState(self):
    return self.lift_state
  def SetState(self, lift_state):
    self.lift_state = lift_state
  def Open(self):
    self.SetState(self.lift_state.Open())
  def Close(self):
    self.SetState(self.lift_state.Close())

  def Run(self):
    self.SetState(self.lift_state.Run())

  def Stop(self):
    self.SetState(self.lift_state.Stop())

# 測試場景
if __name__ == "__main__":
  ctx = Context()
  ctx.SetState(StopState())  # 初始狀態：停止

  ctx.Open()  # 停止 → 開門
  ctx.Run()  # 開門狀態禁止運行
  ctx.Close() # 開門 → 停止
  ctx.Run()  # 停止 → 運行
  ctx.Stop()  # 運行 → 停止
