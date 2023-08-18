import unittest
from peewee import *

from app import TimelinePost


MODELS = [TimelinePost]

# in-memory SQLite for tests
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db
        # Since we have a complete list of all models,
        # we do not need to recursively bind dependencies
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        # Create 2 timeline posts
        first_post = TimelinePost.create(
            name='John Doe', email='john@example.com', content='Hello World, I\'m John!')
        assert first_post.id == 1

        second_post = TimelinePost.create(
            name='Joni Park', email='joni@example.com', content='Hello World, I\'m Joni!')
        assert second_post.id == 2

        # TODO: Get timeline posts and assert that they are correct
        all_posts = TimelinePost.select()

        self.assertEqual(all_posts.count(), 2)

        mock_first_post = all_posts[0]
        self.assertEqual(mock_first_post.name, 'John Doe')
        self.assertEqual(mock_first_post.email, 'john@example.com')
        self.assertEqual(mock_first_post.content, 'Hello World, I\'m John!')

        mock_first_post = all_posts[1]
        self.assertEqual(mock_first_post.name, 'Joni Park')
        self.assertEqual(mock_first_post.email, 'joni@example.com')
        self.assertEqual(mock_first_post.content, 'Hello World, I\'m Joni!')

if __name__== '__main__':
    unittest.main()