"""
"""
from .base import FacilityTestCase


class UserDeletionTestCase(FacilityTestCase):

    def create_user(self, username=None, password=None):
        if not username:
            username = self.data['username']
        if not password:
            password = self.data['password_first']
        user = FacilityUser(username=username, facility=self.facility)
        user.set_password(password)
        user.save()
        return user

    def test_create_duplicate_usernames_via_models(self):
        """We should now be able to create multiple users with the same username/facility combo."""
        self.create_user(username="duplicity", password="firstguy")
        self.create_user(username="duplicity", password="secondguy")
        self.assertEqual(FacilityUser.objects.filter(username="duplicity", facility=self.facility).count(), 2)

    def test_soft_deleting_user_does_work(self):
        user = FacilityUser(username=self.data['username'], facility=self.facility)
        user.set_password('insecure')
        user.save()
        user.soft_delete()
        self.assertTrue(user.deleted)
