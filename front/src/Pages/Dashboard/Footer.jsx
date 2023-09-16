import React from 'react';
import { Outlet, Link } from 'react-router-dom';
import styles from '../../Assets/Styles/Footer.module.scss'
import body from '../../Assets/Styles/Body.module.scss'

function Footer() {
    return (
        <footer  >
            <hr ></hr>
            <div className={`${styles.FooterDiv1} `}>
                <div >
                    <strong> Handmade gifts</strong>
                    <p>
                        From November 2020 we have created our Capricio Store self-service!
                        Our store "Capricio Store" its always opens !
                        Come with Us and Look our Handmade products or contact us if u want to customize an article
                    </p>
                </div>
                {/* <!-- Begin Mailchimp Signup Form --> */}
                <div >
                    <form
                        action="https://herokuapp.us21.list-manage.com/subscribe/post?u=9c82f60c13f5bea1711bf6037&amp;id=8cfce4adf0&amp;f_id=003ad2e1f0"
                        method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form"
                        target="_blank" novalidate>
                        <div className={`${styles.BorderLeft}`}>
                            <h2 >Subscribe </h2>
                            <hr ></hr>
                            <small>To recive our offers and newsletter</small>
                            <div >
                                <span >*</span> indicates required</div>
                            <div >
                                <label for="mce-EMAIL">
                                    Email Address<span >*</span>
                                </label>
                                <input type="email" value="" name="EMAIL" id="mce-EMAIL" required
                                    placeholder="Example@.email.com"></input>
                                <span id="mce-EMAIL-HELPERTEXT"></span>
                            </div>
                            <div id="mce-responses">
                                <div id="mce-error-response" ></div>
                                <div id="mce-success-response" ></div>
                            </div>
                            {/* <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups--> */}
                            <div aria-hidden="true">
                                <label className={styles.Hiden} for="hiden">hiden</label>
                                <input className={styles.Hiden} type="text" id="hiden" name="b_9c82f60c13f5bea1711bf6037_8cfce4adf0"
                                    tabIndex="-1" value=""></input>
                            </div>
                            <div >
                                <div >
                                    <input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe"></input>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
                {/* <!--End mc_embed_signup--> */}

            </div>
            <div className={`${styles.FooterDiv2} `}>
                <div >
                    <h3>Index</h3>
                    <hr className={`${styles.W50}`}></hr>
                    <Link to="/">Home</Link>
                </div>
                <div>
                    <h3 >Information</h3>
                    <hr className={`${styles.W50}`}></hr>
                    <div>
                        <Link to="/ContactUs">Contact</Link>

                    </div>

                    <div>
                        <p>
                        <small>All rights reserved</small>
                        <small>The images used are purely fiction and for academic purposes we do not seek to profit and if
                            there is any copyright problem, please contact us to remove it.</small>
                        </p>
                    </div>
                </div>
                <div>
                    <h3 >Developed By</h3>
                    <hr className={`${styles.W50}`}></hr>
                    <h4>David Hernandez </h4>
                    <a href="https://www.linkedin.com/in/david-hern%C3%A1ndez-b3764b171/" target='_blank'>
                        <ion-icon name="logo-linkedin"></ion-icon> LinkedIn
                    </a>
                </div>
                <div>
                    <h3><strong> Follow Us on </strong></h3>
                    <hr className={`${styles.W50}`}></hr>
                    <div>
                        <a href="https://www.facebook.com/profile.php?id=100089305256045" target="_blank">
                            <ion-icon name="logo-facebook"></ion-icon> Capricio
                        </a>
                    </div>
                </div>
            </div>
        </footer>
    );
}

export default Footer;






