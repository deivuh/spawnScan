# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Inventory/InventoryItemData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Data.Player import PlayerCamera_pb2 as POGOProtos_dot_Data_dot_Player_dot_PlayerCamera__pb2
from POGOProtos.Data.Player import PlayerCurrency_pb2 as POGOProtos_dot_Data_dot_Player_dot_PlayerCurrency__pb2
from POGOProtos.Data.Player import PlayerStats_pb2 as POGOProtos_dot_Data_dot_Player_dot_PlayerStats__pb2
from POGOProtos.Data import PokedexEntry_pb2 as POGOProtos_dot_Data_dot_PokedexEntry__pb2
from POGOProtos.Data import PokemonData_pb2 as POGOProtos_dot_Data_dot_PokemonData__pb2
from POGOProtos.Inventory import AppliedItems_pb2 as POGOProtos_dot_Inventory_dot_AppliedItems__pb2
from POGOProtos.Inventory import Candy_pb2 as POGOProtos_dot_Inventory_dot_Candy__pb2
from POGOProtos.Inventory import EggIncubators_pb2 as POGOProtos_dot_Inventory_dot_EggIncubators__pb2
from POGOProtos.Inventory import InventoryUpgrades_pb2 as POGOProtos_dot_Inventory_dot_InventoryUpgrades__pb2
from POGOProtos.Inventory.Item import ItemData_pb2 as POGOProtos_dot_Inventory_dot_Item_dot_ItemData__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Inventory/InventoryItemData.proto',
  package='POGOProtos.Inventory',
  syntax='proto3',
  serialized_pb=_b('\n,POGOProtos/Inventory/InventoryItemData.proto\x12\x14POGOProtos.Inventory\x1a)POGOProtos/Data/Player/PlayerCamera.proto\x1a+POGOProtos/Data/Player/PlayerCurrency.proto\x1a(POGOProtos/Data/Player/PlayerStats.proto\x1a\"POGOProtos/Data/PokedexEntry.proto\x1a!POGOProtos/Data/PokemonData.proto\x1a\'POGOProtos/Inventory/AppliedItems.proto\x1a POGOProtos/Inventory/Candy.proto\x1a(POGOProtos/Inventory/EggIncubators.proto\x1a,POGOProtos/Inventory/InventoryUpgrades.proto\x1a(POGOProtos/Inventory/Item/ItemData.proto\"\xd2\x04\n\x11InventoryItemData\x12\x32\n\x0cpokemon_data\x18\x01 \x01(\x0b\x32\x1c.POGOProtos.Data.PokemonData\x12\x31\n\x04item\x18\x02 \x01(\x0b\x32#.POGOProtos.Inventory.Item.ItemData\x12\x34\n\rpokedex_entry\x18\x03 \x01(\x0b\x32\x1d.POGOProtos.Data.PokedexEntry\x12\x39\n\x0cplayer_stats\x18\x04 \x01(\x0b\x32#.POGOProtos.Data.Player.PlayerStats\x12?\n\x0fplayer_currency\x18\x05 \x01(\x0b\x32&.POGOProtos.Data.Player.PlayerCurrency\x12;\n\rplayer_camera\x18\x06 \x01(\x0b\x32$.POGOProtos.Data.Player.PlayerCamera\x12\x43\n\x12inventory_upgrades\x18\x07 \x01(\x0b\x32\'.POGOProtos.Inventory.InventoryUpgrades\x12\x39\n\rapplied_items\x18\x08 \x01(\x0b\x32\".POGOProtos.Inventory.AppliedItems\x12;\n\x0e\x65gg_incubators\x18\t \x01(\x0b\x32#.POGOProtos.Inventory.EggIncubators\x12*\n\x05\x63\x61ndy\x18\n \x01(\x0b\x32\x1b.POGOProtos.Inventory.Candyb\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Data_dot_Player_dot_PlayerCamera__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Player_dot_PlayerCurrency__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Player_dot_PlayerStats__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_PokedexEntry__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_PokemonData__pb2.DESCRIPTOR,POGOProtos_dot_Inventory_dot_AppliedItems__pb2.DESCRIPTOR,POGOProtos_dot_Inventory_dot_Candy__pb2.DESCRIPTOR,POGOProtos_dot_Inventory_dot_EggIncubators__pb2.DESCRIPTOR,POGOProtos_dot_Inventory_dot_InventoryUpgrades__pb2.DESCRIPTOR,POGOProtos_dot_Inventory_dot_Item_dot_ItemData__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INVENTORYITEMDATA = _descriptor.Descriptor(
  name='InventoryItemData',
  full_name='POGOProtos.Inventory.InventoryItemData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_data', full_name='POGOProtos.Inventory.InventoryItemData.pokemon_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='POGOProtos.Inventory.InventoryItemData.item', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokedex_entry', full_name='POGOProtos.Inventory.InventoryItemData.pokedex_entry', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_stats', full_name='POGOProtos.Inventory.InventoryItemData.player_stats', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_currency', full_name='POGOProtos.Inventory.InventoryItemData.player_currency', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_camera', full_name='POGOProtos.Inventory.InventoryItemData.player_camera', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_upgrades', full_name='POGOProtos.Inventory.InventoryItemData.inventory_upgrades', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applied_items', full_name='POGOProtos.Inventory.InventoryItemData.applied_items', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_incubators', full_name='POGOProtos.Inventory.InventoryItemData.egg_incubators', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candy', full_name='POGOProtos.Inventory.InventoryItemData.candy', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=477,
  serialized_end=1071,
)

_INVENTORYITEMDATA.fields_by_name['pokemon_data'].message_type = POGOProtos_dot_Data_dot_PokemonData__pb2._POKEMONDATA
_INVENTORYITEMDATA.fields_by_name['item'].message_type = POGOProtos_dot_Inventory_dot_Item_dot_ItemData__pb2._ITEMDATA
_INVENTORYITEMDATA.fields_by_name['pokedex_entry'].message_type = POGOProtos_dot_Data_dot_PokedexEntry__pb2._POKEDEXENTRY
_INVENTORYITEMDATA.fields_by_name['player_stats'].message_type = POGOProtos_dot_Data_dot_Player_dot_PlayerStats__pb2._PLAYERSTATS
_INVENTORYITEMDATA.fields_by_name['player_currency'].message_type = POGOProtos_dot_Data_dot_Player_dot_PlayerCurrency__pb2._PLAYERCURRENCY
_INVENTORYITEMDATA.fields_by_name['player_camera'].message_type = POGOProtos_dot_Data_dot_Player_dot_PlayerCamera__pb2._PLAYERCAMERA
_INVENTORYITEMDATA.fields_by_name['inventory_upgrades'].message_type = POGOProtos_dot_Inventory_dot_InventoryUpgrades__pb2._INVENTORYUPGRADES
_INVENTORYITEMDATA.fields_by_name['applied_items'].message_type = POGOProtos_dot_Inventory_dot_AppliedItems__pb2._APPLIEDITEMS
_INVENTORYITEMDATA.fields_by_name['egg_incubators'].message_type = POGOProtos_dot_Inventory_dot_EggIncubators__pb2._EGGINCUBATORS
_INVENTORYITEMDATA.fields_by_name['candy'].message_type = POGOProtos_dot_Inventory_dot_Candy__pb2._CANDY
DESCRIPTOR.message_types_by_name['InventoryItemData'] = _INVENTORYITEMDATA

InventoryItemData = _reflection.GeneratedProtocolMessageType('InventoryItemData', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYITEMDATA,
  __module__ = 'POGOProtos.Inventory.InventoryItemData_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.InventoryItemData)
  ))
_sym_db.RegisterMessage(InventoryItemData)


# @@protoc_insertion_point(module_scope)
