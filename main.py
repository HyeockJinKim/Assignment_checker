from model.classes import Classes

if __name__ == '__main__':
    classes = Classes.create('checker.csv')
    classes.clone_all()
    classes.update_all()
    classes.test_all()
    classes.score_all()
