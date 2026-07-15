from pages import AddTeamPage, TeamsListPage


def test_team_name_case_insensitive_unique(page):
    """BUG-006: Team names should be case-insensitive unique."""
    add_team = AddTeamPage(page)
    teams_list = TeamsListPage(page)

    add_team.create_team("Engineering")
    add_team.create_team("engineering")

    teams_list.navigate()
    count = teams_list.count_teams_containing("ngineering")
    assert count == 1, (
        f"BUG-006: Found {count} teams with similar names (case-insensitive). "
        "Team names should be case-insensitive unique. "
        "Both 'Engineering' and 'engineering' were created."
    )
