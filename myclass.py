class myclass:


    __privatevar = 27;

    
    def __privmethod(self):
        print("I am inside class myclass ")


    def hello(self):
        print("Private variable value:", myclass.__privatevar)


foo = myclass()
foo.hello()
foo.privmethod()