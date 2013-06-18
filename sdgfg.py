# sdgfg.py
from three import Scene, PerspectiveCamera, WebGLRenderer,CubeGeometry,SphereGeometry,MeshNormalMaterial,Mesh, PlaneGeometry, 
# We will control the horizontal. We will control the vertical.
#from browser import *
import browser
# Discard the old canvas if it exists. 
for canvas in browser.document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

scene = Scene()

# Aspect ratio will be reset in onWindowResize
camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 2

renderer = WebGLRenderer()

container = browser.document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

geometry = PlaneGeometry(1, 1, 1)
#geometry = SphereGeometry(1.0, 32, 24)
material = MeshNormalMaterial()
mesh = Mesh(geometry, material)
scene.add(mesh)

requestID = None
progress = None
progressEnd = 10000
startTime =  None

def render():
    mesh.rotation.x = mesh.rotation.x + 0.02
    mesh.rotation.y = mesh.rotation.y + 0.02
    mesh.rotation.z = mesh.rotation.z + 0.02
        
    renderer.render(scene, camera)

def onWindowResize():
    camera.aspect = browser.window.innerWidth / browser.window.innerHeight
    camera.updateProjectionMatrix()
    renderer.size = (browser.window.innerWidth, browser.window.innerHeight)
    
def step(timestamp):
    global requestID, progress, startTime
    if (startTime):
        progress = timestamp - startTime
    else:
        if (timestamp):
            startTime = timestamp
        else:
            progress = 0
        
    if (progress < progressEnd):
        requestID = browser.window.requestAnimationFrame(step)
        render()
    else:
        browser.window.cancelAnimationFrame(requestID)
        # container.removeChild(renderer.domElement)
        # TODO: Remove the "resize" event listener

browser.window.addEventListener("resize", onWindowResize, False)

onWindowResize()

step(None)