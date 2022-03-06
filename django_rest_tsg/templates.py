from string import Template

INTERFACE_TEMPLATE = Template(
    """export interface $name {
$fields
}"""
)
INTERFACE_FIELD_TEMPLATE = Template("  $name: $type;")
ENUM_TEMPLATE = Template(
    """export enum $name {
$members
}"""
)
ENUM_MEMBER_TEMPLATE = Template("  $name = $value")
IMPORT_TEMPLATE = Template("import { $type } from '$filename';\n")
HEADER_TEMPLATE = Template(
    """// This file is generated by $generator@$version
// You are strongly advised not to manually change this file for backend consistency.
// Source Type: $type
// Last modified on: $date
"""
)
