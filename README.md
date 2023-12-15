# crawler
This contains the files from my discord bot, crawler, coded in Python 3.6.11


11/25/2023
  Changed actions to a overrideable function in the entity class. May be annoying (or not) when I make interactables that do not do attacking or moving an entity but will be solved in the future. 
  Now planning edits to create enemy to begin testing attack action. After attack action is startup cleanup, mutators (one of each), then room creation.

11/22/2023
  Move function is now complete, put in actions.py. Added an offline (non-bot connected) main, which means extra maintenance but doesn't necessarily need this maintenance.
  Changed how functions are... functioning. Now mainly using: create, do, view so that things are uniform. also main bot now has "admin" commands.
  Finished the move function, it is part of the action file, but may be moved to the map file so that there are less passing arguments (the action debate)
  Currently avoiding structural decisions and going to begin work on enemy entity so that I can begin work to test a mutator
    
11/19/2023
  Currently attempting a move function via the actions.py file. Conditions, actions, and mutators are effectively empty. Maps is still filler. Playerlist needs edits to adopt the use of mutators to read in players properly (right now it is filler)

12/15/2023
  Changed the structure of the code to include folders, as the amount of files were being quite heavy. Fixed a bug related to the "view character short" function since the actions changed. Added a parameter to map creation to streamline further map testing. Added "entityList" to map.py in order to make finding entities on the map faster (previously was iterating the entire map), additionally added a position attribute to all entities.
