### ARGS ###

iterations = 10;
gridWidth = 20;


## Vars ##

indentLevel = 0;
file = None

def indent():
	indentLevel = indentLevel + 1

def deindent():
	indentLevel = indentLevel - 1

def newline():
	printcode( "" )

def printCode( code ):
	file.print( "\t" * indentLevel )
	file.println( code )

## These things are constant for any size
def generateIntro():
	printCode( 'Make Laura moan' )
	printCode( 'Make Julia moan "#00000001#"' )
	newline()

	printCode( 'Make startString moan "#0"' )
	printCode( 'Make endString moan "0#"' )
	newline()

	printCode( 'Lick AsciiZero forty eight times' )
	printCode( 'Lick AsciiOne forty nine times' )
	printCode( 'Lick AsciiOcto\'s thigh thirty five times' )
	newline()

	printCode ( "Worship Counter" )
	printCode ( "Worship iterations" )
	newline()
	
	printCode( "Worship left" )
	printCode( "Worship middle" )
	printCode( "Worship right" )
	newline()
	newline()
	newline()

## A better solution would write the string literal for the number, but this is generated code, so allow my laziness.
def generateNumbers():
	printCode( "Worship number0" )
	for i in range( 1, gridWidth-1 ):
		variableName = number + str( i )
		for j in range (0, i):
			printCode( "lick" + variableName )
	newline()
	newline()

def beginLoop():
	printCode( "while iterations is submissive to Number" + str(iterations) )
	indent()
	newline()
	newline()

def setEmptyPositions():
	for i in range (2, gridWidth - 3):
		printCode( "make position" + str(i) + " moan")
		printCode( "make nextposition" + str(i) + " moan")
	newline()
	newline()

def resetTempVariables():
	printCode( "Have left spank left" )
	printCode( "Have middle spank middle" )
	printCode( "Have right spank right" )

def incrementLoopCounter():
	printCode( "lick counter" )
	newline()

def printCurrentState():
	printCode( "Make Slave Scream Julia" )
	newline()

def generateParentString( pos ):
	printcode( "If counter is submissive to number" + str( pos + 2 ) )
	indent()
	printcode( "If counter is dominant towards number" + str( pos -2 ) )
	indent()
	printcode( "Have Emma hogtie position" + str( pos ) )
	unindent()
	unindent()
	newline()	

#This function is the main trick to running the 110. 
#For each cell, we create a string that contains three chars: 
#The ones relevant to it's activation.
def getParentStrings():
	printcode( "Bind Emma to Julia" )
	indent()
	printcode( "If Emma is not AsciiOcto" )
	indent()
	for i in range (2, gridWidth - 3)
		generateParentString( i )
	deindent()
	printcode( "lick counter" )

def getDescendants():
	


def getDescendant( pos ):
	printCode( "Have counter spank counter" )
	printCode( "Have left spank left" )
	printCode( "Have middle spank middle" )
	printCode( "Have right spank right" )
	newline()
	newline()

	printcode( "Bind Emma to position" + str( pos ) )
	indent()
	printcode( "if counter is number0" )
	indent()
	printCode( "If Emma is AsciiZero" )
	indent()
	printCode( "Have AsciiZero lick left" )
	deindent()
	printCode( "Otherwise" )
	indent()
	printCode( "Have AsciiOne lick left" )
	deindent()
	deindent()
	printCode( "if counter is number1" )
	indent()
	printCode( "If Emma is AsciiZero" )
	indent()
	printCode( "Have AsciiZero lick middle" )
	deindent()
	printCode( "Otherwise" )
	indent()
	printCode( "Have AsciiOne lick middle" )
	deindent()
	deindent()
	printCode( "if counter is number2" )
	indent()
	printCode( "If Emma is AsciiZero" )
	indent()
	printCode( "Have AsciiZero lick right" )
	deindent()
	printCode( "Otherwise" )
	indent()
	printCode( "Have AsciiOne lick right" )
	deindent()
	deindent()
	printCode( "Lick counter" )
	newline()
	newline()


	printCode( "if left is AsciiOne" )
	indent()
	printCode( "if middle is AsciiOne" )
	indent()
	printCode( "if right is AsciiZero" )
	indent()
	printCode( "Have AsciiOne hogtie nextposition" + str( pos ) )
	deindent()
	printCode( "otherwise" )
	indent()
	printCode( "have AsciiZero hogtie nextposition" + str( pos ) )
	deindent()
	deindent()
	printCode( "if middle is AsciiZero" )
	indent()
	printCode( "if right is AsciiOne" )
	indent()
	printCode( "have AsciiOne hogtie nextposition" + str( pos ) )
	deindent()
	printCode( "otherwise" )
	indent()
	printCode( "have AsciiZero hogtie nextposition" + str( pos ) )
	deindent()
	deindent()
	deindent()
	printCode( "if left is AsciiZero" )
	indent()
	printCode( "if middle is AsciiOne" )
	indent()
	printCode( "Have AsciiOne hogtie nextposition" + str( pos ) )
	deindent()
	printCode( "otherwise" )
	indent()
	printCode( "if right is AsciiOne" )
	indent()
	printCode( "Have AsciiOne hogtie nextposition" + str( pos ) )
	deindent()
	printCode( "otherwise" )
	indent()
	printCode( "have AsciiZero hogtie nextposition" + str( pos ) )
	deindent()
	deindent()
	deindent()

	newline()
	newline()
	newline()


def main():
	global file
	with open("110-generated.fet", "rw") as file:
		generateIntro()
		generateNumbers()
		beginLoop()
		resetTempVariables()
		setEmptyPositions()
		incrementLoopCounter()
		printCurrentState()
		getParentStrings()



