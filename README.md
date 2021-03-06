# pyjama
___

## Run python scripts in browser
  1. add python script to db folder
  2. commit changes to git
  3. push to master branch
  4. push to heroku
  5. visit `wrlowc.herokuapp.com/py/{the name of the script}`
  
     examples: 
       - `wrlowc.herokuapp.com/py/test1`  
       - `wrlowc.herokuapp.com/py/test2`
       - `wrlowc.herokuapp.com/py/test_args?params=ben sat on a log`  
     
## Run local server
  1. cd into the main folder
  2. run `node app.js`
  3. visit `http://localhost:4000/` in the browser

## Push changes to the repo
In the terminal:
  1. git add .
  2. git commit -m "{details of the change}"
  3. git push origin master
  4. git push heroku master
  
___

## dinodb.py examples
- Add record:
  - `py dinodb.py add ben hello-to-the-world` (need to replace spaces with -)
  
- Get record:
  - `py dinodb.py get {id}`
  - `py dinodb.py get all`
  
- Edit record:
  - `py dinodb.py edit {id}`
  
- Delete record:
  - `py dinodb.py del {id}`
  - `py dinodb.py del all`
