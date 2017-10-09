### ARGS ###

iterations = 40;
gridWidth = 40;


## Vars ##

indentLevel = 0;
file = open("110-generated.fet", "w")

def indent():
	global indentLevel
	indentLevel = indentLevel + 1

def unindent():
	global indentLevel
	indentLevel = indentLevel - 1

def newline():
	printCode( "" )

def printCode( code ):
	global indentLevel
	file.write( "\t" * indentLevel )
	file.write( code )
	file.write( "\n" )

## These things are constant for any size
def generateIntro():
	printCode( 'Make Laura moan' )
	printCode( 'Make Julia moan "#' + "0" * (gridWidth-3) + '1#"' )
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
	for i in range( 1, max(gridWidth - 1, iterations)+1 ):
		variableName = "number" + str( i )
		for j in range (0, i):
			printCode( "lick " + variableName )
	newline()
	newline()

def beginLoop():
	printCode( "while iterations is submissive to Number" + str(iterations) )
	indent()
	newline()
	newline()

def setEmptyPositions():
	for i in range (2, gridWidth - 2):
		printCode( "make position" + str(i) + " moan")
		printCode( "make nextposition" + str(i) + " moan")
	newline()
	newline()

def resetTempVariables():
	printCode( "Have left spank left" )
	printCode( "Have middle spank middle" )
	printCode( "Have right spank right" )
	printCode( "Have counter spank counter" )
	printCode( "Make Laura moan" )
	newline()

def incrementLoopCounter():
	printCode( "lick iterations" )
	newline()

def printCurrentState():
	printCode( "Make Slave Scream Julia" )
	newline()

def generateParentString( pos ):
	printCode( "If counter is submissive to number" + str( pos + 2 ) )
	indent()
	printCode( "If counter is dominant towards number" + str( pos -2 ) )
	indent()
	printCode( "Have Emma hogtie position" + str( pos ) )
	unindent()
	unindent()
	newline()	

#This function is the main trick to running the 110. 
#For each cell, we create a string that contains three chars: 
#The ones relevant to it's activation.
def getParentStrings():
	printCode( "Bind Emma to Julia" )
	indent()
	printCode( "If Emma is not AsciiOcto" )
	indent()
	for i in range (2, gridWidth - 2):
		generateParentString( i )
	unindent()
	printCode( "lick counter" )
	unindent()
	newline()
	newline()
	newline()

def getDescendants():
	for i in range (2, gridWidth - 2):
		getDescendant( i )
	newline()
	newline()
	newline()



def getDescendant( pos ):
	printCode( "Have counter spank counter" )
	printCode( "Have left spank left" )
	printCode( "Have middle spank middle" )
	printCode( "Have right spank right" )
	newline()
	newline()

	printCode( "Bind Emma to position" + str( pos ) )
	indent()
	printCode( "if counter is number0" )
	indent()
	printCode( "If Emma is AsciiZero" )
	indent()
	printCode( "Have AsciiZero lick left" )
	unindent()
	printCode( "Otherwise" )
	indent()
	printCode( "Have AsciiOne lick left" )
	unindent()
	unindent()
	printCode( "if counter is number1" )
	indent()
	printCode( "If Emma is AsciiZero" )
	indent()
	printCode( "Have AsciiZero lick middle" )
	unindent()
	printCode( "Otherwise" )
	indent()
	printCode( "Have AsciiOne lick middle" )
	unindent()
	unindent()
	printCode( "if counter is number2" )
	indent()
	printCode( "If Emma is AsciiZero" )
	indent()
	printCode( "Have AsciiZero lick right" )
	unindent()
	printCode( "Otherwise" )
	indent()
	printCode( "Have AsciiOne lick right" )
	unindent()
	unindent()
	printCode( "Lick counter" )
	unindent()
	newline()
	newline()


	printCode( "if left is AsciiOne" )
	indent()
	printCode( "if middle is AsciiOne" )
	indent()
	printCode( "if right is AsciiZero" )
	indent()
	printCode( "Have AsciiOne hogtie nextposition" + str( pos ) )
	unindent()
	printCode( "otherwise" )
	indent()
	printCode( "have AsciiZero hogtie nextposition" + str( pos ) )
	unindent()
	unindent()
	printCode( "if middle is AsciiZero" )
	indent()
	printCode( "if right is AsciiOne" )
	indent()
	printCode( "have AsciiOne hogtie nextposition" + str( pos ) )
	unindent()
	printCode( "otherwise" )
	indent()
	printCode( "have AsciiZero hogtie nextposition" + str( pos ) )
	unindent()
	unindent()
	unindent()
	printCode( "if left is AsciiZero" )
	indent()
	printCode( "if middle is AsciiOne" )
	indent()
	printCode( "Have AsciiOne hogtie nextposition" + str( pos ) )
	unindent()
	printCode( "otherwise" )
	indent()
	printCode( "if right is AsciiOne" )
	indent()
	printCode( "Have AsciiOne hogtie nextposition" + str( pos ) )
	unindent()
	printCode( "otherwise" )
	indent()
	printCode( "have AsciiZero hogtie nextposition" + str( pos ) )
	unindent()
	unindent()
	unindent()

	newline()
	newline()
	newline()


def writeNextGeneration():
	printCode( "make Laura moan \"#0\"" )
	for i in range (2, gridWidth - 2):
		writeNextGenerationPosition( i )
	printCode( "have AsciiZero hogtie Laura" )
	printCode( "have AsciiOcto hogtie Laura" )
	newline()
	newline()
	newline()

def writeNextGenerationPosition( pos ):
	printCode( "bind Emma to nextposition" + str( pos ) )
	indent()
	printCode( "if Emma is AsciiZero" )
	indent()
	printCode( "have AsciiZero hogtie Laura" )
	unindent()
	printCode( "otherwise" )
	indent()
	printCode( "have AsciiOne hogtie Laura" )
	unindent()
	unindent()

def saveNextGeneration():
	printCode( "Make Julia moan" )
	printCode( "bind Emma to Laura" )
	indent()
	printCode( "have Emma hogtie Julia" )


def main():
	generateIntro()
	generateNumbers()
	beginLoop()
	resetTempVariables()
	setEmptyPositions()
	incrementLoopCounter()
	printCurrentState()
	getParentStrings()
	getDescendants()
	writeNextGeneration()
	saveNextGeneration()

main()
