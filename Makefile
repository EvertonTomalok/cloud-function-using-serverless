public:
	gcloud functions add-iam-policy-binding $(function) --member="allUsers" --role="roles/cloudfunctions.invoker" --project=$(project) --region=us-east1
