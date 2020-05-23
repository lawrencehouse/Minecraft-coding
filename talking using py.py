from mcpi.minecraft import Minecraft # Needed for API communication

mc = Minecraft.create() # Needed for API communication
talk = "WORKS GOOD TO ME!!!" 
mc.postToChat(talk)
