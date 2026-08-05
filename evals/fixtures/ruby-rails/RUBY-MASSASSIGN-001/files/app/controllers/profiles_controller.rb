class ProfilesController < ApplicationController
  before_action :authenticate_user!

  def update
    # Vulnerable: permits every attribute the client sends, including
    # email_verified, which the profile update form never legitimately
    # sets. A crafted request body can flip email_verified to true without
    # completing the verification flow.
    current_user.update(profile_params)
    redirect_to profile_path, notice: "Profile updated."
  end

  private

  def profile_params
    params.require(:user).permit!
  end
end
