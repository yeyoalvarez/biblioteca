// Modules to control application life and create native browser window
const {app, BrowserWindow} = require('electron')
const path = require('path')

function createWindow() {

	var subpy = require('child_process').spawn('python', ['./manage.py', 'runserver']);
    var rq = require('request-promise');
    var mainAddr = 'http://localhost:8000';
    var openWindow = function() {
        mainWindow = new BrowserWindow({ width: 800, height: 600 })
        mainWindow.loadURL('http://localhost:8000');
        mainWindow.on('closed', function() {
            mainWindow = null;
            subpy.kill('SIGINT');
        })
    }
    var startUp = function() {
        rq(mainAddr)
            .then(function(htmlString) {
                console.log('Django iniciado!');
                openWindow();
            })
            .catch(function(err) {
                startUp();
            });
    };
    startUp();
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  createWindow()

  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
