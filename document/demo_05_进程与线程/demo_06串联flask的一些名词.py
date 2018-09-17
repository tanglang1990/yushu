
# 以线程ID号作为key的字典->Local->LocalStack

# AppContext RequestContext -> LocalStack

# Flask -> AppContext   Request -> RequestContext

# current_app ->(LocalStack.top = AppContext top.app=Flask)

# request ->(LocalStack.top = RequestContext top.request= Request)