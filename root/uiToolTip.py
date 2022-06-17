''' 1. '''
# Search @ class ItemToolTip @ def __init__
		self.itemVnum = 0

# Add below
		self.metinSlot = []

''' 2. '''
# Search @ class ItemToolTip @ def __del__
		ToolTip.__del__(self)

# Add below
		self.metinSlot = None

''' 3. '''
# Search @ class ItemToolTip @ def AddItemData
		self.itemVnum = itemVnum

# Add below
		self.metinSlot = metinSlot

''' 4. '''
# Search @ class ItemToolTip @ def AddItemData
		if 50026 == itemVnum:

# Add above
		self.__CalculateToolTipWidth()

''' 5. '''
# Search
	def __SetSkillBookToolTip

# Add above
	def ResizeToolTipWidth(self, width):
		self.toolTipWidth = width

	def __CalculateToolTipWidth(self):
		if self.itemVnum == 0:
			return

		item.SelectItem(self.itemVnum)
		if item.GetItemDescription():
			return

		affectTextLineLenList = []

		metinSocket = self.metinSlot
		if metinSocket:
			for socketIndex in metinSocket:
				if socketIndex:
					item.SelectItem(socketIndex)

					affectType, affectValue = item.GetAffect(0)
					affectString = self.__GetAffectString(affectType, affectValue)
					if affectString:
						affectTextLineLenList.append(len(affectString))

		if self.toolTipWidth == self.TOOL_TIP_WIDTH:
			if affectTextLineLenList:
				self.toolTipWidth += max(affectTextLineLenList) + 10

		self.AlignTextLineHorizonalCenter()
