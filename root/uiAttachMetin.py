''' 1. '''
# Search @ class AttachMetinDialog @ def Open
		item.SelectItem(metinIndex)

# Add below
		metinSubType = item.GetItemSubType()

''' 2. '''
# Search @ class ItemToolTip @ def Open
		## Old Item ToolTip
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(player.GetItemMetinSocket(targetItemPos, i))
		self.oldToolTip.AddItemData(itemIndex, metinSlot)

# Replace with
		## New Item ToolTip
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(player.GetItemMetinSocket(targetItemPos, i))
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			slotData = metinSlot[i]
			if self.CanAttachMetin(slotData, metinSubType):
				metinSlot[i] = metinIndex
				break
		self.newToolTip.AddItemData(itemIndex, metinSlot)

''' 3. '''
# Search @ class ItemToolTip @ def Open
		## New Item ToolTip
		item.SelectItem(metinIndex)
		metinSubType = item.GetItemSubType()

		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(player.GetItemMetinSocket(targetItemPos, i))
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			slotData = metinSlot[i]
			if self.CanAttachMetin(slotData, metinSubType):
				metinSlot[i] = metinIndex
				break
		self.newToolTip.AddItemData(itemIndex, metinSlot)

# Replace with
		## Old Item ToolTip
		item.SelectItem(metinIndex)
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(player.GetItemMetinSocket(targetItemPos, i))
		self.oldToolTip.ResizeToolTipWidth(self.newToolTip.GetWidth())
		self.oldToolTip.AddItemData(itemIndex, metinSlot)

''' 4. '''
# Search @ class ItemToolTip @ def UpdateDialog
		newWidth = self.newToolTip.GetWidth() + 230 + 15 + 20

# Replace with
		newWidth = 15 + self.oldToolTip.GetWidth() + 45 + self.newToolTip.GetWidth() + 15

''' 5. '''
# Search @ class ItemToolTip @ def UpdateDialog
		newHeight = self.newToolTip.GetHeight() + 98

# Add below
		self.newToolTip.SetPosition(15 + self.oldToolTip.GetWidth() + 45, 38)