from app import form_app
from flask_script import Manager,Server


app =form_app('development')

manager = Manager(app)
manager.add_commmand('server, Server')

@manager.command
def test():
    '''
    It will run the unittest
    '''
    import unittest
    test = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(test)



if __name__ == '__main__':
    manager.working()