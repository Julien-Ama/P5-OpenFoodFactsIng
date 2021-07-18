from Engine.Reception import Reception
from Engine.Engine import Engine

if __name__ == '__main__':
    myEngine = Engine
    hasData = myEngine.checkData
    myReception = Reception()
    myReception.home(hasData)
