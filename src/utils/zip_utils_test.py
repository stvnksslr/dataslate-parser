from pathlib import Path
from unittest import TestCase

from src.utils.zip_utils import check_if_zipped


class ZipUtilsTest(TestCase):
    def setUp(self):
        self.base_path = Path.cwd() / "test_rosters"
        self.zipped_kill_team_roster = str(
            self.base_path / "zipped_rosters" / "elite_roster.rosz"
        )
        self.unzipped_kill_team_roster = str(
            self.base_path / "kill_team" / "elite_roster.ros"
        )

    async def test__zipped_roster(self):
        roster_file = await check_if_zipped(self.zipped_kill_team_roster)
        self.assertTrue(roster_file)

    async def test__unzipped_roster_is_formatted_correctly(self):
        roster_file = await check_if_zipped(self.zipped_kill_team_roster)

        self.assertEqual(self.zipped_kill_team_roster, roster_file)
