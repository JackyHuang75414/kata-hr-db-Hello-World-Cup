from pages import AddTeamPage, TeamsListPage


def test_create_team(page):
    add_team = AddTeamPage(page)
    teams_list = TeamsListPage(page)

    add_team.create_team("my team")
    teams_list.navigate()
    assert teams_list.is_team_visible("my team")
