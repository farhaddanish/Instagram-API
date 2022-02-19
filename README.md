# Instagram-API
this is sample Insatgram API


# Instagram APi

## Introduction

this is a sample api that you can use in your next project.
this is a api that user can create thier own profile, post, follow and unfollow system. 
this is include all instagram features.
also i have added some permissions, filtering,  and authentication service.
this api made in djangorestframework that i used python and django based languages and frameworks.


## Code Samples

class AllFollowers (generics.ListAPIView):
    queryset = UserFollowing.objects.all()
    serializer_class = Followers_serializer
    def get_queryset(self):
        pk = self.kwargs["pk"]
        profile = Profile_users.objects.get(pk=pk)
        followers = UserFollowing.objects.filter(followers=profile)
        return followers


class CreatePostGV (generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Posts.objects.all()
    serializer_class = Post_serializers
    def perform_create(self, serializer):
        user = self.request.user
        profile = Profile_users.objects.get(user=user)
        profile.posts_count += 1
        profile.save()
        serializer.save(profile=profile)
        return serializer
        
        
        
class SinglePostGV (APIView):
    permission_classes = [PostUpdatePermission, IsAuthenticated]
    def get(self, request, pk, pk2):
        post = Posts.objects.get(pk=pk2)
        serializer = Post_serializers(post)
        return Response(serializer.data)
    def put(self, request, pk, pk2):
        post = Posts.objects.get(pk=pk2)
        self.check_object_permissions(request, post)
        serializer = Post_serializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self, request, pk, pk2):
        post = Posts.objects.get(pk=pk2)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_200_OK)
        
        
        

## Installation

first you should install all requirments on your virtual enviroment then do all migrations and use all these endpoints

there is some endpoints that you can use
# all Profiles
loaclhost/profiles/
# single profile
loaclhost/profiles/id/
# alll post of individual profile
loaclhost/profiles/id/posts/
# single post
loaclhost/profiles/id/post/id/
# createpost
loaclhost/profiles/createpost
# register
loaclhost/acccount/register/
# edit profile
loaclhost/account/register/id/profile/
# makefollow
loaclhost/profiles/id/makefollow
# allfollowers of single profile
loaclhost/profiles/id/followers/
# allfollowing of single profile
loaclhost/profiles/id/following/
# unfollow
loaclhost/profiles/id/unfollow

