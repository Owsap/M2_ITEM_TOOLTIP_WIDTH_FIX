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
		if not item.GetItemDescription():
			self.__CalculateToolTipWidth()

''' 5. '''
# Search
	def __SetSkillBookToolTip

# Add above
	def ResizeToolTipWidth(self, width):
		self.toolTipWidth = width

	def __CalculateToolTipWidth(self):
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

			if self.itemVnum:
				item.SelectItem(self.itemVnum)
			self.metinSlot = None

		if self.toolTipWidth == self.TOOL_TIP_WIDTH:
			if affectTextLineLenList:
				self.toolTipWidth += max(affectTextLineLenList) + 10

		self.AlignTextLineHorizonalCenter()

''' 6. '''
# Search @ class ItemToolTip
	def AutoAppendTextLine(self, text, color = FONT_COLOR, centerAlign = True):

# Add above
	def AlignTextLineHorizonalCenter(self):
		for child in self.childrenList:
			if type(child).__name__ == "TextLine":
				(x, y) = child.GetLocalPosition()
				child.SetPosition(self.toolTipWidth / 2, y)

		self.ResizeToolTip()