from django.test import TestCase
from django.urls import reverse
from nippo.models import NippoModel

class NippoTestCase(TestCase):
    #初期設定
    def setUp(self):
        obj = NippoModel(title="testTitle1", content="testContent1")
        obj.save()

    #日報の作成ができているか
    def test_saved_single_object(self):
        qs_counter = NippoModel.objects.count()
        self.assertEqual(qs_counter, 1)
    
    #queryが存在しない時に、404ページを返すかどうか
    def test_response_404(self):
        detail_url = reverse('nippo-detail', kwargs={"pk": 100})
        detail_response = self.client.get(detail_url)
        update_url = reverse('nippo-update', kwargs={"pk": 100})
        update_response = self.client.get(update_url)
        delete_url = reverse('nippo-delete', kwargs={"pk": 100})
        delete_response = self.client.get(delete_url)
        self.assertEqual(detail_response.status_code, 404)
        self.assertEqual(update_response.status_code, 404)
        self.assertEqual(delete_response.status_code, 404)

    #createページできちんとデータが保存されているか
    def test_create_on_createView(self):
        url = reverse('nippo-create')
        create_data = {"title": "title_from_test", "content": "content_from_test"}
        response = self.client.post(url, create_data)
        qs_counter2 = NippoModel.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(qs_counter2, 2)
        
    def test_listview_with_anonymous(self):
        url = reverse("nippo-list")
        response = self.client.get(url)
        object_list = response.context_data["object_list"]
        self.assertEqual(len(object_list), 0)

    def test_listview_with_own_user(self):
        url = reverse("nippo-list")
        self.client.login(email=self.email, password=self.password)
        response = self.client.get(url)
        object_list = response.context_data["object_list"]
        self.assertEqual(len(object_list), 1)
        
    def make_user_to_create_2_nippo(self, email, pwd="test_pass", number=2):
        user_obj = User(email=email)
        user_obj.set_password(pwd)
        user_obj.save()
        email_obj = EmailAddress(user=user_obj, email=email, verified=True)
        email_obj.save()
        for i in range(number):
            nippo_obj = self.make_nippo(user=user_obj, public=True)
        return user_obj
    
    #（テスト関数ではない）日報リストプロフィールページから一覧を取得
    def get_nippo_by_profile(self, user_obj):
        self.client.force_login(user_obj)
        url = reverse("nippo-list") + f"?profile={user_obj.profile.id}"
        response = self.client.get(url)
        filter = response.context_data["filter"]
        return len(filter.qs)
        
    #profileページのテスト
    def test_profile_page(self):
        #メインユーザーの日報数を数えて、表示の確認
        main_user_nippo = NippoModel.objects.filter(user=self.user_obj).count()
        profile_list_counter = self.get_nippo_by_profile(self.user_obj)
        self.assertTrue(main_user_nippo, profile_list_counter)
        #ほかのユーザーを作成してテスト（自動で2つ日報が作られる）
        how_many_made_by_another = 3
        another_user1 = self.make_user_to_create_2_nippo(email="abc_another1@itc.tokyo", number=how_many_made_by_another)
        another_profile_list_counter = self.get_nippo_by_profile(another_user1)
        self.assertTrue(how_many_made_by_another, another_profile_list_counter)
        
        #ほかのユーザーを作成してテスト（自動で2つ日報が作られる）
        how_many_made_by_another2 = 5
        another_user2 = self.make_user_to_create_2_nippo(email="abc_another2@itc.tokyo", number=how_many_made_by_another2)
        another_profile_list_counter2 = self.get_nippo_by_profile(another_user1)
        self.assertTrue(how_many_made_by_another2, another_profile_list_counter2)