hotbar = [
  'Torch',
  'Rock',
  'Potion',
  'Sword',
  'Shield'
]
sword_index = hotbar.index('Sword')
sword_remover = hotbar.pop(sword_index)
hotbar.insert(0, sword_remover)
print(hotbar)
