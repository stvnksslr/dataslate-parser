def get_rules_summary(parsed_list):
    rules_summary = {}
    for squad in parsed_list:
        for unit in squad.list_of_units:
            rules_summary.update(unit.abilities)
    return rules_summary
